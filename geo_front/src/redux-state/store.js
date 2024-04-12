import { configureStore } from '@reduxjs/toolkit'
import counterReducer from './reducers/red'
export const store = configureStore({
  reducer: {
    counter: counterReducer,
  },
})
