import React, { useEffect, useState } from "react";
import {MapContainer, TileLayer, Marker} from "react-leaflet";
import { useMapEvent } from 'react-leaflet/hooks'
import L from "leaflet";

delete L.Icon.Default.prototype._getIconUrl;

L.Icon.Default.mergeOptions({
  iconRetinaUrl: require("leaflet/dist/images/marker-icon-2x.png"),
  iconUrl: require("leaflet/dist/images/marker-icon.png"),
  shadowUrl: require("leaflet/dist/images/marker-shadow.png")
});
const MyMap = () => {
    function MyComponent() {
      const [position, setPosition] = useState(null);

      const map = useMapEvent('click', (e) => {
          setPosition(e.latlng)
          console.log(e.latlng)

      })
      return position === null ? null : <Marker position={position}></Marker>
    }
  return (
          <React.Fragment>
              <MapContainer center={[55.753247, 37.620914]} zoom={11}>
                  <TileLayer
                      attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                      url="https://cartodb-basemaps-{s}.global.ssl.fastly.net/light_all/{z}/{x}/{y}.png"/>
                <MyComponent/>
              </MapContainer>
          </React.Fragment>
      )
}

export default MyMap;

