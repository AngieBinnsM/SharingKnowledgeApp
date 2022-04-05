import React from 'react'
import { Navbar } from 'react-bootstrap'
import icon from './NavBarImg.png'

function NavBar() {
  return (
    <Navbar bg='primary' variant='dark'>
      <Navbar.Brand href='#home'>
        <img alt='' src={icon} width='80' height='70' /> Sharing Knowledge App
      </Navbar.Brand>
    </Navbar>
  )
}
export default NavBar