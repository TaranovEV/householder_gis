import React from "react";
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import MyMap from "../views/global/MyMap";
import MyButton from "../comps/Button";
import MySpan from "../comps/Span";
import StickyHeadTable from "../comps/Table";
import {opponentsColumns , opponentsRows, ourShopsColumns, ourShopsRows, publicTransportColumns, publicTransportRows, subwayColumns, subwaytRows} from '../../data.jsx';
import {useNavigate} from "react-router-dom";
import { useState } from 'react';


export default function ResultCalcPage() {
    let navigate = useNavigate();
    const routeChange = () =>{
    let path = `/`;
    navigate(path);
  }
    const menuItemsVehType = [
        "auto",
        "walk"
    ]
    const menuItemsTimeLen = [
        "5",
        "10"
    ]
    const quatersCount = 13258

  return (
    <Box className="foo" sx={{display: 'flex', height: '100vh', overflow : 'auto'}} flexDirection={"row"}>
      <Box className="a" sx={{width: 1/4, height: '100vh', bgcolor:"#082032", overflow: 'auto'}}>
        <Grid item  margin={"20px 20px 20px 20px"}>
            <MySpan items={menuItemsVehType} labelId={"moveTypeLabel"} id={"moveType"} text={`Зона влияния: ${menuItemsVehType[0]}  ${menuItemsTimeLen[0]} мин.`}></MySpan>
            <MySpan items={menuItemsTimeLen} labelId={"timeLenLabel"} id={"timeLen"} text={`Домохозяйства: ${quatersCount} шт.`}></MySpan>
            <MySpan items={menuItemsTimeLen} labelId={"timeLenLabel"} id={"timeLen"} text={`Конкуренты:`}></MySpan>
            <StickyHeadTable columns={opponentsColumns} rows={opponentsRows}></StickyHeadTable>
        </Grid>
          <Grid item margin={"10px 20px 20px 20px"}>
              <MySpan items={menuItemsTimeLen} labelId={"timeLenLabel"} id={"timeLen"} text={`Магазины сети:`}></MySpan>
              <StickyHeadTable columns={ourShopsColumns} rows={ourShopsRows}></StickyHeadTable>
          </Grid>
          <Grid item margin={"10px 20px 20px 20px"}>
              <MySpan items={menuItemsTimeLen} labelId={"timeLenLabel"} id={"timeLen"} text={`Общественный транспорт (300 м):`}></MySpan>
              <StickyHeadTable columns={publicTransportColumns} rows={publicTransportRows}></StickyHeadTable>
          </Grid>
                    <Grid item margin={"10px 20px 20px 20px"}>
              <MySpan items={menuItemsTimeLen} labelId={"timeLenLabel"} id={"timeLen"} text={`Метро(зона влияния):`}></MySpan>
              <StickyHeadTable columns={subwayColumns} rows={subwaytRows}></StickyHeadTable>
          </Grid>
          <Grid item alignItems={"stretch"} margin={"10px 20px 20px 20px"}>
              <MyButton label={"Очистить"} onClick={routeChange}></MyButton>
          </Grid>
      </Box>
        <Box className="bc" sx={{display: 'flex', flex: 1, overflow: 'scroll'}} flexDirection={"column"}>
          <MyMap/>
        </Box>
    </Box>
  );
}
