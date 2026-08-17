import { useState } from "react"
import { useNavigate } from "react-router-dom"
import axios from "axios"

function Login() {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    email: "",
    password: "",
  });
  const [message, setMessage] = useState(null);
  const [isError, setIsError] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = new URLSearchParams();
    data.append("username", formData.email);
    data.append("password", formData.password);

    try {
      const response = await axios.post("http://localhost:8000/login", data, {
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
      });

      localStorage.setItem("access_token", response.data.access_token);
      setMessage(response.data.message || "Login successful");
      setIsError(false);
      navigate('/dashboard');
    } catch (error) {
      const detail = error.response?.data?.detail || "Login failed.";
      setMessage(detail);
      setIsError(true);
    }
  };

  return (
    <div className="auth-page">
      <div className="auth-card">
        <div className="auth-card__header">
          <h2>Welcome back</h2>
          <p>Sign in to continue to your workspace</p>
        </div>

        <form className="auth-form" onSubmit={handleSubmit}>
          <label className="auth-field">
            <span>Email or username</span>
            <input
              type="email"
              placeholder="Enter your email"
              required
              value={formData.email}
              onChange={(e) => setFormData({ ...formData, email: e.target.value })}
            />
          </label>

          <label className="auth-field">
            <span>Password</span>
            <input
              type="password"
              placeholder="Enter your password"
              value={formData.password}
              required
              onChange={(e) => setFormData({ ...formData, password: e.target.value })}
            />
          </label>

          <button className="auth-button" type="submit">
            Login
          </button>

          {message ? (
            <p className={`auth-message ${isError ? "auth-message--error" : ""}`}>
              {message}
            </p>
          ) : null}
        </form>

        <p className="auth-switch">
          Don’t have an account?
          <button type="button" className="auth-link-button" onClick={() => navigate("/register")}>
            Register
          </button>
        </p>
      </div>
    </div>
  );
}

export default Login