import axios from 'axios';
import jwt from 'jsonwebtoken';

const BASEURL = 'http://localhost:5000';

class BoltAPI {
  static async getUserFromAPI(data) {
    let token = await axios.post(`${BASEURL}/login`, data);
    console.log('token');
    let payload = jwt.decode(token.data.token);
    localStorage.setItem('token', token.data.token);
    let user = await axios({
      method: 'get',
      url: `${BASEURL}/users/${payload.identity.id}`,
      headers: {
        Authorization: 'Bearer ' + token
      }
    });
    localStorage.setItem('user', JSON.stringify(user.data));
    return user.data;
  }
}

export default BoltAPI;
