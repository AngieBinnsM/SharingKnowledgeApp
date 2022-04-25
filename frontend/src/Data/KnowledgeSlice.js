import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";

export const getIdeas = createAsyncThunk(
  "ideas/getIdeas",
  async (dispatch, getState) => {
    return await fetch(
      " https://cbx3peeaah.execute-api.us-east-1.amazonaws.com/dev/get-ideas"
    ).then((res) => res.json());
  }
);

export const putIdea = createAsyncThunk("ideas/putIdea", async (payload) => {
  const { id, user, technology, title, link, description } = payload.load;
  return await fetch(
    " https://cbx3peeaah.execute-api.us-east-1.amazonaws.com/dev/put-ideas",
    {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        id,
        user,
        technology,
        title,
        link,
        description,
      }),
    }
  ).then((res) => res.json());
});

export const deleteIdea = createAsyncThunk(
  "ideas/deleteIdea",
  async (payload) => {
    return await fetch(
      `https://cbx3peeaah.execute-api.us-east-1.amazonaws.com/dev/delete-idea?technology=${payload.technology}&id=${payload.id}`,
      {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
        },
      }
    ).then((res) => res.json());
  }
);

const initialState = {
  idea: [],
  mode: false,
  modeContent: "",
};

const customerSlice = createSlice({
  // An unique name of a slice
  name: "Knowledge",

  // Initial state value of the reducer
  initialState,

  // Reducer methods
  reducers: {
    noValue: (state) => {
      state.mode = true;
      state.modeContent = "Please write your discovery";
    },

    noModeContent: (state) => {
      state.mode = false;
    },
  },

  extraReducers: {
    [getIdeas.fulfilled]: (state, action) => {
      state.idea = action.payload;
    },

    [putIdea.fulfilled]: (state, action) => {
      state.idea.push(action.payload);
      state.mode = true;
      state.modeContent = "New knowledge added";
    },

    [deleteIdea.fulfilled]: (state, action) => {
      const newItem = state.idea.filter(
        (point) => point.id !== action.payload.id
      );
      return {
        ...state,
        idea: newItem,
      };
    },
  },
});

// Action creators for each reducer method
export const { noValue, noModeContent } = customerSlice.actions;

export default customerSlice.reducer;
