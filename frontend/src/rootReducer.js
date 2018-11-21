import { GOT_USER } from './actionTypes';

const initialState = { currUser: null, workspaces: [] };

function rootReducer(state = initialState, action) {
  switch (action.type) {
    case GOT_USER:
      let newState = { ...state };
      return (newState.currUser = action.payload); //{ ...state, currUser: action.payload };
    default:
      return state;
  }
}

export default rootReducer;
