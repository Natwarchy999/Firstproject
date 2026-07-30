import { useState } from "react"
import axios from "axios"

function Login(){

 const [formData ,setFormData] = useState({
     email: "",
     password: ""
    })
 const [message,setMessage]=useState(null)
    
    
    const handleSubmit= async (e)=>{
        e.preventDefault();
        const  data = new URLSearchParams();
        data.append('username',formData.email)
        data.append('password',formData.password)

        try {
            const response=await axios.post(
                    "http://localhost:8000/login",
                    data,
                    { headers: {"Content-Type": "application/x-www-form-urlencoded"}
            });

            setMessage(response.data.message)
            
        }
        catch(error){
            setMessage(error.response.data.detail)
        }

        localStorage.setItem("access_token",response.data.access_token)

    }

return(
    <>
    <div style={styles.container}>
    <form style={styles.card} onSubmit={handleSubmit}>

        <input
         type="email"
         placeholder="Email or username"
         required
         value={formData.email}
         onChange={(e)=>setFormData({...formData,email:e.target.value})}
         />

        <input
         type="password"
         placeholder="Password"
         value={formData.password}
         required
         onChange={(e) => setFormData({ ...formData, password: e.target.value })}
         />
         <button type="submit">Login</button>
         {message ? <p style={styles.message}>{message}</p> : null}
    </form>
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

export default Login