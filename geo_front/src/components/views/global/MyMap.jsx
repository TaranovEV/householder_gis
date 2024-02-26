import React from "react";
import {MapContainer, TileLayer} from "react-leaflet";


const MyMap = () => {
    return (
        <React.Fragment>
            <MapContainer center={[55.753247, 37.620914]} zoom={11}>
                <TileLayer
                    attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                    url="https://cartodb-basemaps-{s}.global.ssl.fastly.net/light_all/{z}/{x}/{y}.png"/>
            </MapContainer>
        </React.Fragment>
    )
}

export default MyMap;

