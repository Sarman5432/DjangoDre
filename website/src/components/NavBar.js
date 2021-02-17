import React from 'react'
import { Navbar as Nav } from "react-bootstrap";

export default function NavBar() {
  return (
    <Nav bg="dark" variant="dark" fixed="top">
      <Nav.Brand className="m-auto">
        <h4>Kounter Shot!</h4>
      </Nav.Brand>
    </Nav>
  );
}
