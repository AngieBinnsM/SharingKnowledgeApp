import React from 'react'
import img from './icon2.png'
import Form from '../Form/Form'
import { Card } from 'react-bootstrap'
import { body, secondBody, thirdBody } from './style'

function CardPresentation() {
  return (
    <div style={body}>
      <div style={thirdBody}>
        <Card style={secondBody}>
          <img src={img} style={{ width: '250px', margin: '20px' }} />
          <Card.Body>
            <Card.Title>Sharing Knowledge App</Card.Title>
            <Form></Form>
          </Card.Body>
        </Card>
      </div>
    </div>
  )
}

export default CardPresentation