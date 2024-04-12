import React, {useEffect, useState} from "react";
import {MapContainer, Marker, Polygon, TileLayer, LayersControl, LayerGroup, Popup} from "react-leaflet";
import {useMap, useMapEvent} from 'react-leaflet/hooks'
import L from "leaflet";
import {useDispatch, useSelector} from "react-redux";
import {changeCoord} from '../../../redux-state/reducers/red'
import { useLocation } from 'react-router-dom';
import { Icon } from "leaflet";
import metroSvg from "../../../svg/moscowmetro.svg";
import oppoShopSvg from "../../../svg/oppo.svg";
import ourShopSvg from "../../../svg/oursShop.svg";
import busSvg from "../../../svg/bus.svg";

delete L.Icon.Default.prototype._getIconUrl;

L.Icon.Default.mergeOptions({
  iconRetinaUrl: require("leaflet/dist/images/marker-icon-2x.png"),
  iconUrl: require("leaflet/dist/images/marker-icon.png"),
  shadowUrl: require("leaflet/dist/images/marker-shadow.png")
});

const MyMap = (props) => {
  const [coordinates, setCoordinates] = useState([]);
  const [markersMetro, setMarkersMetro] = useState([]);
  const [markersOppo, setMarkersOppo] = useState([]);
  const [markersOur, setMarkersOur] = useState([]);
  const [markersBus, setMarkersBus] = useState([]);

  const mertoIcon = new Icon({
    iconUrl:  metroSvg,
    iconSize: [30, 100],
    iconAnchor: [15, 100],
    popupAnchor: [-25, -40],
    backgroundColor: 'green'
  });
  const oppoShopIcon = new Icon({
    iconUrl:  oppoShopSvg,
    iconSize: [20, 20],
    iconAnchor: [10, 20],
    popupAnchor: [-25, -40],
  });
  const ourShopIcon = new Icon({
    iconUrl:  ourShopSvg,
    iconSize: [20, 20],
    iconAnchor: [10, 20],
    popupAnchor: [-25, -40],
  });
  const busIcon = new Icon({
    iconUrl:  busSvg,
    iconSize: [20, 20],
    iconAnchor: [10, 20],
    popupAnchor: [-25, -40],
  });

  useEffect(() => {
    setCoordinates(props.geometry.map((row) => [row[1], row[0]]));
  }, [props.geometry.length]);

  useEffect(() => {
    setMarkersMetro(props.markersMetro.map((row) => [row.geometry.coordinates[1], row.geometry.coordinates[0]]));
  }, [props.markersMetro.length]);

  useEffect(() => {
    setMarkersOppo(props.markersOppo.map((row) => [row.geometry.coordinates[1], row.geometry.coordinates[0]]));
  }, [props.markersOppo.length]);

  useEffect(() => {
    setMarkersOur(props.markersOur.map((row) => [row.geometry.coordinates[1], row.geometry.coordinates[0]]));
  }, [props.markersOur.length]);

  useEffect(() => {
    setMarkersBus(props.markersBus.map((row) => [row.geometry.coordinates[1], row.geometry.coordinates[0]]));
  }, [props.markersBus.length]);

  const usePathname = () => {
    const location = useLocation();
    return location.pathname;
  }
  function CutFlag(){
        const map = useMap()
        map.attributionControl.setPrefix('')
    }
  function MarkerComponent() {
    const dispatch = useDispatch()
    const position = useSelector(state => state.counter.position)
    const clickOnMap = useMapEvent('click', (e) => {
        dispatch(changeCoord(e.latlng))
      })
    return position === null ? null : <Marker position={position}></Marker>
    }
  return (
          <React.Fragment>
              <MapContainer center={props.center} zoom={props.zoom}>
                  <TileLayer
                      attribution='Data by &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>,
                      under <a href="https://opendatacommons.org/licenses/odbl/">ODbL.</a>'
                      url="https://cartodb-basemaps-{s}.global.ssl.fastly.net/light_all/{z}/{x}/{y}.png"/>
                  <CutFlag/>
                {usePathname() === '/calculate/' && <MarkerComponent/>}
                {props.pinCoords.length && <Marker position={[props.pinCoords[1], props.pinCoords[0]]}></Marker>}
                {props.geometry.length && <Polygon positions={coordinates}/>}

                <LayersControl position="topright">
                  <LayersControl.Overlay name="Opponents">
                    <LayerGroup>
                      {props.markersOppo.length && markersOppo.map((coordinates) =>
                          <Marker position={coordinates} icon={oppoShopIcon}>
                          {/*<Popup>*/}
                          {/*  <span>A pretty CSS3 popup. <br/> Easily customizable.</span>*/}
                          {/*</Popup>*/}
                        </Marker>
                        )}
                      </LayerGroup>
                    </LayersControl.Overlay>

                  <LayersControl.Overlay name="Our Shops">
                    <LayerGroup>
                      {props.markersOur.length && markersOur.map((coordinates) =>
                          <Marker position={coordinates} icon={ourShopIcon}>
                          {/*<Popup>*/}
                          {/*  <span>A pretty CSS3 popup. <br/> Easily customizable.</span>*/}
                          {/*</Popup>*/}
                        </Marker>
                        )}
                    </LayerGroup>
                  </LayersControl.Overlay>

                  <LayersControl.Overlay name="Metro Stations">
                    <LayerGroup>
                      {props.markersMetro.length && markersMetro.map((coordinates) =>
                          <Marker position={coordinates} icon={mertoIcon}>
                          {/*<Popup>*/}
                          {/*  <span>A pretty CSS3 popup. <br/> Easily customizable.</span>*/}
                          {/*</Popup>*/}
                        </Marker>
                        )}
                      </LayerGroup>
                    </LayersControl.Overlay>

                  <LayersControl.Overlay name="Bus Stops">
                    <LayerGroup>
                      {props.markersBus.length && markersBus.map((coordinates) =>
                          <Marker position={coordinates} icon={busIcon}>
                          {/*<Popup>*/}
                          {/*  <span>A pretty CSS3 popup. <br/> Easily customizable.</span>*/}
                          {/*</Popup>*/}
                        </Marker>
                        )}
                    </LayerGroup>
                  </LayersControl.Overlay>
                </LayersControl>
              </MapContainer>
          </React.Fragment>
      )
}

export default MyMap;
