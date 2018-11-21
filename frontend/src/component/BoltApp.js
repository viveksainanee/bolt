import React, { Component } from 'react';
import Dashboard from './Dashboard';
import Portal from './Portal';
import { connect } from 'react-redux';
import './BoltApp.css';
import { getUser } from '../actions';

class BoltApp extends Component {
  async componentDidMount() {
    console.log('component did mount');
    if (localStorage.getItem('currUser')) {
      await this.props.getUser();
      console.log('found a user');
    }
    console.log('no user');
  }

  render() {
    // return <Portal />;
    console.log('Boltapp rendered');
    // return <div>{this.props.currUser ? <Dashboard /> : <Portal />}</div>;
    return <Dashboard />;
  }
}

function mapStateToProps(state) {
  return { currUser: state.currUser };
}
export default connect(
  mapStateToProps,
  { getUser }
)(BoltApp);
