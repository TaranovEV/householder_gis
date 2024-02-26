import React from "react";
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import MyMap from "../views/global/MyMap";
import BasicSelect from "../comps/Select";
import MyButton from "../comps/Button";
import {useNavigate} from "react-router-dom";

export default function calcPage() {
  const menuItemsVehType = [
        "auto",
        "walk"
    ]
    const menuItemsTimeLen = [
        "5 мин",
        "10 мин"
    ]
  let navigate = useNavigate();
  const routeChange = (event) =>{
    console.log(event)
    if (1) {
      let path = `/result/`;
      navigate(path)
    }
    else {
      alert('Укажите точку расчета!')
    }
  }


  return (
    <Box className="foo" sx={{display: 'flex',height: '100vh'}} flexDirection={"row"}>
      <Box className="a" sx={{width: 1/4, height: '100%', bgcolor:"#082032"}}>
        <Grid item  margin={"100px 20px 20px 20px"}>
            <BasicSelect items={menuItemsVehType} labelId={"moveTypeLabel"} id={"moveType"}></BasicSelect>
        </Grid>
          <Grid item margin={"10px 20px 20px 20px"}>
              <BasicSelect items={menuItemsTimeLen} labelId={"timeLenLabel"} id={"timeLen"}></BasicSelect>
          </Grid>
          <Grid item alignItems={"stretch"} margin={"10px 20px 20px 20px"}>
              <MyButton label={"Рассчитать"} onClick={routeChange}></MyButton>
          </Grid>
      </Box>
        <Box className="bc" sx={{display: 'flex', flex: 1}} flexDirection={"column"}>
          <MyMap/>
        </Box>
    </Box>
  );
}
