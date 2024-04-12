import React from "react";
import {useSelector} from 'react-redux'
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import MyMap from "../views/global/MyMap";
import BasicSelect from "../comps/Select";
import CustomButton from "../comps/Button";
import {Navigate, useLocation, useNavigate} from "react-router-dom";
import CircularDownloadData from "../comps/ProgressPreload"
import axios from 'axios';
import {handleLogOut} from "../../logic/functions";
import {baseApiUrl} from "../../constants";

export default function calcPage() {
  const handleLogOut = (event) => {
    localStorage.setItem('accessToken', null)
    localStorage.setItem('refreshToken', null)
    navigate('/')
  }
  const coord = useSelector(state => state.counter.position)
  const menuItemsVehType = [
        "auto",
        "walk"
    ]
    const menuItemsTimeLen = [
        "5 мин",
        "10 мин"
    ]
  const [selectVehType, setSelectVehType] = React.useState('');
  const [selectTimeLen, setSelectTimeLen] = React.useState('');
  const location = useLocation();
  const handleChangeVehType = (event) => {
    setSelectVehType(event.target.value);
  };
    const handleChangeTimeLen = (event) => {
    setSelectTimeLen(event.target.value);
  };

  let navigate = useNavigate();
  const [isLoading, setLoading] = React.useState(false);
  const getIso = async (e) => {

    if (selectVehType === '' || selectTimeLen === '' || coord === null ){
      alert('Укажите время и тип передвижения !')
    }
    else{
      setLoading(true)
      const newStr = localStorage.getItem('accessToken').replace(/"/g, '')
        const response = await axios.get(
          `${baseApiUrl}/api/map/calculate/`,
          {
            headers: {'accept': 'application/json',
                      Authorization: "Bearer " + newStr},
            params: {
              lat: encodeURIComponent(coord.lat),
              lon: encodeURIComponent(coord.lng),
              type_iso: encodeURIComponent(selectVehType),
              time_iso: encodeURIComponent(selectTimeLen)
            }}).then(response => {
              console.log(response.data)
              const data = response.data
              navigate('/result/', {state: data})
            }).catch (error => {
              console.log(error)
              alert('Back')
             }).then(function (response){
               setLoading(false)
      })
    }
  }

  return (
    <Box className="foo" sx={{display: 'flex',height: '100vh'}} flexDirection={"row"}>
      <Box className="a" sx={{width: 1/4, height: '100%', bgcolor:"#082032"}} >
        <Box sx={{ flexGrow: 1 }} margin={"20px 20px 20px 20px"}>
          <Grid container spacing={3}>
            <Grid item xs>
            </Grid>
            <Grid item xs={6}>
            </Grid>
            <Grid item xs>
              <CustomButton label={"LOGOUT"} onClick={handleLogOut}></CustomButton>
            </Grid>
          </Grid>
        </Box>
        <Grid item  margin={"20px 20px 20px 20px"}>
            <BasicSelect onChangeItem={handleChangeVehType} it={selectVehType} items={menuItemsVehType} labelId={"moveTypeLabel"} id={"moveType"} key={"moveType"}></BasicSelect>
        </Grid>
          <Grid item margin={"10px 20px 20px 20px"}>
              <BasicSelect onChangeItem={handleChangeTimeLen} it={selectTimeLen} items={menuItemsTimeLen} labelId={"timeLenLabel"} id={"timeLen"} key={"timeLen"}></BasicSelect>
          </Grid>
          <Grid item alignItems={"stretch"} margin={"10px 20px 20px 20px"}>
              <CustomButton disable={isLoading ?true: false} label={"Рассчитать"} onClick={getIso}></CustomButton>
          </Grid>
      </Box>
        <Box className="bc" sx={{display: 'flex', flex: 1}} flexDirection={"column"}>
          <MyMap geometry={[]} zoom={12} center={[55.753247, 37.620914]} markersMetro={[]} markersOppo={[]} markersOur={[]} markersBus={[]} pinCoords={[]}/>
        </Box>
    </Box>
  );
}
