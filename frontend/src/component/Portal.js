import React, { Component } from 'react';
import RoutesPortal from './RoutesPortal';

class Portal extends Component {
  render() {
    console.log('Portal rendered');
    return <RoutesPortal />;
  }
}

export default Portal;
