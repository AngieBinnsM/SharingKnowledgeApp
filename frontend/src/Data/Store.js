import { configureStore } from '@reduxjs/toolkit'
import KnowledgeReducer from './KnowledgeSlice'

export const store = configureStore({
  reducer: {
    knowledge: KnowledgeReducer,
  },
})