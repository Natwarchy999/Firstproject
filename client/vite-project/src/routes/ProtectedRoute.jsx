import { Navigate , replace, useLocation} from "react-router-dom";

function ProtectedRoute({children}){
    const location=useLocation();
    const token=sessionStorage.getItem("access_token");
    if(!token){
        return (<Navigate to='/dashbord' replace state={{from:location}}/>)
    }
    return children;
}
export default ProtectedRoute;