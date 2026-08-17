import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function Register() {
  const navigate = useNavigate();
  const [form, setForm] = useState({
    name: "",
    email: "",
    password: "",
  });

  const [message, setMessage] = useState(null);
  const [isError, setIsError] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post("http://localhost:8000/register", form);
      setMessage(response.data.message || "Registration successful");
      setIsError(false);
    } catch (error) {
      const detail = error.response?.data?.detail || "Registration failed.";
      setMessage(detail);
      setIsError(true);
    }
  };

  return (
    <div className="auth-page">
      <div className="auth-card">
        <div className="auth-card__header">
          <h2>Create account</h2>
          <p>Join us and start managing your tasks</p>
        </div>

        <form className="auth-form" onSubmit={handleSubmit}>
          <label className="auth-field">
            <span>Full name</span>
            <input
              placeholder="Enter your name"
              type="text"
              value={form.name}
              required
              onChange={(e) => setForm({ ...form, name: e.target.value })}
            />
          </label>

          <label className="auth-field">
            <span>Email address</span>
            <input
              placeholder="Enter your email"
              type="email"
              value={form.email}
              required
              onChange={(e) => setForm({ ...form, email: e.target.value })}
            />
          </label>

          <label className="auth-field">
            <span>Password</span>
            <input
              placeholder="Enter your password"
              type="password"
              value={form.password}
              required
              onChange={(e) => setForm({ ...form, password: e.target.value })}
            />
          </label>

          <button className="auth-button" type="submit">
            Register
          </button>

          {message ? (
            <p className={`auth-message ${isError ? "auth-message--error" : ""}`}>
              {message}
            </p>
          ) : null}
        </form>

        <p className="auth-switch">
          Already have an account?
          <button type="button" className="auth-link-button" onClick={() => navigate("/login")}>
            Login
          </button>
        </p>
      </div>
    </div>
  );
}

export default Register