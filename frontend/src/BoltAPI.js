import axios from 'axios';
import jwt from 'jsonwebtoken';

const BASEURL = 'http://localhost:5000';

class BoltAPI {
  static async getUserFromAPI(data) {
    if (localStorage.getItem('currUser')) {
      return JSON.parse(localStorage.getItem('currUser'));
    }

    let token = await axios.post(`${BASEURL}/login`, data);
    let payload = jwt.decode(token.data.data.token);
    localStorage.setItem('token', token.data.data.token);
    let user = await axios({
      method: 'get',
      url: `${BASEURL}/users/${payload.identity}`,
      headers: {
        Authorization: 'Bearer ' + token
      }
    });
    localStorage.setItem('currUser', JSON.stringify(user.data.data));
    return user.data.data;
  }
}

export default BoltAPI;
