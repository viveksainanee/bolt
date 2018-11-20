import { GOT_USER } from './actionTypes';

const initialState = { currUser: null, workspaces: [] };

function rootReducer(state = initialState, action) {
  switch (action.type) {
    case GOT_USER:
      return { ...state, currUser: action.payload.data };
    default:
      return state;
  }
}

export default rootReducer;
