import { createSlice } from '@reduxjs/toolkit'

const initialState = {
  position: null,
}

export const counterSlice = createSlice({
  name: 'counter',
  initialState,
  reducers: {
    changeCoord: (state, action) => {
      state.position = action.payload
    },
  },
})

// Action creators are generated for each case reducer function
export const { changeCoord } = counterSlice.actions

export default counterSlice.reducer
