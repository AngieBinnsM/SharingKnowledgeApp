import { createSlice } from '@reduxjs/toolkit'

const initialState = {
  idea: [],
  mode: false,
  modeContent: ''
}

const customerSlice = createSlice({
  // An unique name of a slice
  name: 'Knowledge',

  // Initial state value of the reducer
  initialState,

  // Reducer methods
  reducers: {
    addKnowledge: (state, action) => {
      state.idea.push(action.payload.load)
      state.mode = true
      state.modeContent = 'New knowledge added'
    },

    noValue: (state) => {
      state.mode = true
      state.modeContent = 'Please write your discovery'
    },

    noModeContent: (state) => {
      state.mode = false
    },

    deletee: (state, action) => {
      const newItem = state.idea.filter(
        (point) => point.id !== action.payload.id
      )
      return {
        ...state,
        idea: newItem,
      }
    },
  },
})

// Action creators for each reducer method
export const { addKnowledge, noValue, noModeContent, deletee} =
  customerSlice.actions

export default customerSlice.reducer