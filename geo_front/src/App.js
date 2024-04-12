import React, {useContext} from 'react';
import CalcPage from "./components/pages/calcPage";
import ResultCalcPage from "./components/pages/resultCalcPage";
import {Route, Routes, useLocation, Navigate} from "react-router-dom";
import FormLogin from "./components/views/local/FormLogin";
import FormRegister from "./components/views/local/FormRegister";
import {UserContext} from "./context/UserContext";

function RequireAuth({ children }) {
    const {setAccessToken, setRefreshToken, accessToken, refreshToken} = useContext(UserContext)[0]
    let location = useLocation();
    if (accessToken === 'null'||refreshToken === 'null')  {
      setAccessToken(null)
      setRefreshToken(null)
      return <Navigate to="/" state={{ from: location }} replace />;
  }
  return children;
}

export default function App() {
  return (
        <React.Fragment>
            <Routes>
              <Route path={"/calculate/"} element={<RequireAuth> <CalcPage/> </RequireAuth>}/>
                <Route path={"/"} element={<FormLogin/>}/>
                <Route path={"/result/"} element={<RequireAuth> <ResultCalcPage/> </RequireAuth>}/>
                <Route path={"/register/"} element={<FormRegister/>}/>
            </Routes>
        </React.Fragment>
  );
}
