import ReactDOM from "react-dom/client";
import React from "react";
import "./styles.css";
import 'leaflet/dist/leaflet.css';
import { BrowserRouter } from "react-router-dom";
import { store } from './redux-state/store';
import { Provider } from 'react-redux';
import {UserProvider} from "./context/UserContext";

import App from "./App";

const root = ReactDOM.createRoot(document.getElementById("root"))

root.render(
  <React.StrictMode>

    <BrowserRouter>

        <Provider store={store}>
          <UserProvider>
          <App />
          </UserProvider>
        </Provider>

    </BrowserRouter>

  </React.StrictMode>
);
