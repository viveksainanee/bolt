import React, { Component } from 'react';
import Dashboard from './Dashboard';
import Portal from './Portal';
import { connect } from 'react-redux';
import './BoltApp.css';
import { getUser } from '../actions';

class BoltApp extends Component {
  async componentDidMount() {
    if (localStorage.getItem('currUser')) {
      await this.props.getUser();
    }
  }

  render() {
    return <div>{this.props.currUser ? <Dashboard /> : <Portal />}</div>;
  }
}

function mapStateToProps(state) {
  return { currUser: state.currUser };
}
export default connect(
  mapStateToProps,
  { getUser }
)(BoltApp);
