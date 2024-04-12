import React from "react";
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import MyMap from "../views/global/MyMap";
import CustomButton from "../comps/Button";
import MySpan from "../comps/Span";
import StickyHeadTable from "../comps/Table";
import {opponentsColumns , ourShopsColumns, publicTransportColumns, subwayColumns} from '../../constants.jsx';
import {Navigate, useLocation, useNavigate} from "react-router-dom";
import {useDispatch, useSelector} from "react-redux";
import {changeCoord} from "../../redux-state/reducers/red";


export default function ResultCalcPage(state) {
  const handleLogOut = (event) => {
    localStorage.setItem('accessToken', null)
    localStorage.setItem('refreshToken', null)
    navigate('/')
  }
  const center = useSelector(state => state.counter.position)
  if (center) {
      const arr = Object.entries(center).reduce((acc, [key, value]) => {
    acc.push({key: key, ...value})
    return acc
    }, []);
  }
  const arr = []
  let navigate = useNavigate();
  const location = useLocation();
  const routeChange = () =>{
    dispatch(changeCoord(null))
    navigate('/calculate/');
  }
  const dispatch = useDispatch()
  const typeIso = location.state.features.properties.type_iso
  const timeIso = location.state.features.properties.time_iso
  const routesCount = location.state.features.properties.routes_count
  const quatersCount = location.state.features.properties.quarters_count
  const opponents = location.state.features.properties.opponents_for_render.features
  const opponentsRows = opponents.map(item => (item.properties))
  const ourShops = location.state.features.properties.our_shops_for_render.features
  const ourShopsRows = ourShops.map(item => (item.properties))
  const subwayRows = location.state.features.properties.metro_count
  const publicTransportRows = location.state.features.properties.bus_station
  const pinCoords = location.state.features.properties.pin_coords
  console.log(publicTransportRows)

  return (
    <Box className="foo" sx={{display: 'flex', height: '100vh', overflow : 'auto'}} flexDirection={"row"}>
      <Box className="a" sx={{width: 1/4, height: '100vh', bgcolor:"#082032", overflow: 'auto'}}>
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
            <MySpan labelId={"moveTypeLabel"} id={"moveType"} text={`Зона влияния: ${typeIso}  ${timeIso} мин.`}></MySpan>
            <MySpan labelId={"timeLenLabel"} id={"timeLen"} text={`Домохозяйства: ${quatersCount} шт.`}></MySpan>
            <MySpan labelId={"timeLenLabel"} id={"timeLen"} text={`Конкуренты:`}></MySpan>
            <StickyHeadTable columns={opponentsColumns} rows={opponentsRows}></StickyHeadTable>
        </Grid>
          <Grid item margin={"10px 20px 20px 20px"}>
              <MySpan labelId={"timeLenLabel"} id={"timeLen"} text={`Магазины сети:`}></MySpan>
              <StickyHeadTable columns={ourShopsColumns} rows={ourShopsRows}></StickyHeadTable>
          </Grid>
          <Grid item margin={"10px 20px 20px 20px"}>
              <MySpan labelId={"timeLenLabel"} id={"timeLen"} text={`Общественный транспорт (300 м):`}></MySpan>
              <StickyHeadTable columns={publicTransportColumns} rows={publicTransportRows}></StickyHeadTable>
          </Grid>
                    <Grid item margin={"10px 20px 20px 20px"}>
              <MySpan labelId={"timeLenLabel"} id={"timeLen"} text={`Метро(зона влияния):`}></MySpan>
              <StickyHeadTable columns={subwayColumns} rows={subwayRows}></StickyHeadTable>
          </Grid>
          <Grid item alignItems={"stretch"} margin={"10px 20px 20px 20px"}>
              <CustomButton label={"Очистить"} onClick={routeChange}></CustomButton>
          </Grid>
      </Box>
        <Box className="bc" sx={{display: 'flex', flex: 1, overflow: 'scroll'}} flexDirection={"column"}>
          <MyMap geometry={location.state.features.geometry} zoom={14} center={center? center : [55.753247, 37.620914]} pinCoords={pinCoords} markersOppo={opponents} markersOur={ourShops} markersMetro={subwayRows} markersBus={publicTransportRows} />
        </Box>
    </Box>
  );
}
