import React from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { deletee } from '../../Data/KnowledgeSlice'
import { Button } from 'react-bootstrap'
import { Card } from 'react-bootstrap'
import { body } from './style'
import ReactPlayer from 'react-player'

function SmallCard() {
  const know = useSelector((state) => state.knowledge.idea)
  const dispatch = useDispatch()
  return (
    <section style={body}>
      {know.map((point) => (
        <Card
          style={{
            width: '27rem',
            boxShadow: '0 0 12px rgba(0,0,0,0.5)',
            borderRadius: '15px',
          }}
        >
          <Card.Body>
            <ReactPlayer
              url={point.link}
              controls='true'
              width='400px'
              height='200px'
              muted='false'
            ></ReactPlayer>
            <Card.Header>
              <Card.Title>{point.technology}</Card.Title>
            </Card.Header>

            <Card.Subtitle
              className='mb-2 text-muted'
              style={{ marginTop: '10px' }}
            >
              {point.title}
            </Card.Subtitle>
            <Card.Text>{point.description}</Card.Text>
            <footer className='blockquote-footer'>{point.user}</footer>
            <a href={point.link} className='btn btn-secondary me-2' target='_'>
              Link
            </a>
            <Button
              variant='primary'
              onClick={() => dispatch(deletee({ id: point.id }))}
            >
              Delete
            </Button>
          </Card.Body>
        </Card>
      ))}
    </section>
  )
}

export default SmallCard