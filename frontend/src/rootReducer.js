import { GOT_USER } from './actionTypes';

const initialState = { currUser: null, workspaces: [] };

function rootReducer(state = initialState, action) {
  console.log('state', state, 'action', action);
  switch (action.type) {
    case GOT_USER:
      let newState = { ...state };
      newState.currUser = action.payload;
      console.log((newState.currUser = action.payload));
      return newState; //{ ...state, currUser: action.payload };
    default:
      return state;
  }
}

export default rootReducer;
