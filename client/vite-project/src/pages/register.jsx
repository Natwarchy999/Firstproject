import { useState } from "react";
import axios from "axios" 

function Register(){
    
  const [form ,setForm]=useState({
    name:"",
    email:"",
    password:""
  })
  
  const [message,setMessage]=useState(null)

  const handleSubmit = async (e)=>{
    e.preventDefault();

    try{
      const response=await axios.post("http://localhost:8000/register",form);
      console.log(response.data.message)
      setMessage(response.data.message)

    }

    catch(error) {
        console.log(error.response.data)
        console.log(error.response.data.detail)
        setMessage(error.response.data.detail)
    }
  };

return (
    <>
   <div style={styles.container}>

    <form style={styles.card} onSubmit={handleSubmit}>
      <input 
      placeholder="Enter your name"
      type="text"
      value={form.name}
      required
      onChange={(e)=>setForm({...form,name:e.target.value})}
      />

      <input 
      placeholder="Enter your email"
      type="email"
      value={form.email}
      required
      onChange={(e)=>setForm({...form,email:e.target.value})}
      />

      <input 
      placeholder="Enter your password"
      type="password"
      value={form.password}
      r
      onChange={(e)=>setForm({...form,password:e.target.value})}
      />
      <button type="submit">Register</button>
     </form>
     <button type="submit">Login</button>
         {message ? <p style={styles.message}>{message}</p> : null}

   </div>
    </>
  )
}

const styles = {
  container: {
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    height: "100vh",
  },
  card: {
    display: "flex",
    flexDirection: "column",
    gap: "15px",
    width: "300px",
  },
  message: {
    margin: 0,
    color: "green",
  },
}

export default Register