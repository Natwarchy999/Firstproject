import { BrowserRouter } from 'react-router-dom'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App'
import Register from './pages/register'

createRoot(document.getElementById('root')).render(
<BrowserRouter>
{/* <Register/> */}
<App/>
</BrowserRouter>
)
