import { GOT_USER } from './actionTypes.js';
import BoltAPI from './BoltAPI';

export function getUser(data) {
  return async function(dispatch) {
    let user = await BoltAPI.getUserFromAPI(data);
    console.log('user is', user);
    dispatch(gotUser(user));
  };
}

function gotUser(payload) {
  return {
    type: GOT_USER,
    payload
  };
}
