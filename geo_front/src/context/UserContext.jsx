import React, {createContext, useEffect, useState} from "react";
import {baseApiUrl} from "../constants";

export const UserContext = createContext();

export const UserProvider = (props) => {
  const [accessToken, setAccessToken] = useState(localStorage.getItem('accessToken'));
  const [refreshToken, setRefreshToken] = useState(localStorage.getItem('refreshToken'));

  useEffect(() => {
    const fetchUser = async () => {
      const requestGetOptions = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          'accept': 'application/json',
        },
        body: JSON.stringify(
          {token: localStorage.getItem('accessToken')}
            )
      };
      const requestRefreshPostOptions = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          'accept': 'application/json',},
        body: JSON.stringify(
          {refresh: localStorage.getItem('refreshToken')}
            )
      };
      const response = await fetch(`${baseApiUrl}/api/token/verify/`, requestGetOptions).then((response) => {
            if (!response.ok){
              setAccessToken(null)
              const responseRefresh = fetch(`${baseApiUrl}/api/token/refresh/`, requestRefreshPostOptions);
              if (!responseRefresh.ok){
                setAccessToken(null)
                setRefreshToken(null)
                localStorage.setItem('accessToken', null)
                localStorage.setItem('refreshToken', null)
              } else{
                localStorage.setItem('accessToken', JSON.stringify(responseRefresh.data.access))
                localStorage.setItem('refreshToken', JSON.stringify(responseRefresh.data.refresh))
              }
            }
    }).catch(error => console.error(error))
    fetchUser();
  }}, [accessToken, refreshToken])

  const contextData = {
    setAccessToken: setAccessToken,
    setRefreshToken: setRefreshToken,
    accessToken: accessToken,
    refreshToken: refreshToken,
  }
  return (
    <UserContext.Provider value={[contextData]}>
      {props.children}
    </UserContext.Provider>
  )
}
