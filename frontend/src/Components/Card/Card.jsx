import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Button } from "react-bootstrap";
import { Card } from "react-bootstrap";
import { body, card, search, enter } from "./style";
import ReactPlayer from "react-player";
import CardImg from "./CardImg.jpg";
import { getIdeas, deleteIdea } from "../../Data/KnowledgeSlice";

function SmallCard() {
  const know = useSelector((state) => state.knowledge.idea);
  const dispatch = useDispatch();
  const [searchTerm, setSearchTerm] = useState("");

  useEffect(() => {
    dispatch(getIdeas());
  }, [dispatch]);

  function startWith(str) {
    return str.startsWith("https://www.youtube.com/");
  }

  return (
    <section>
      <div style={search}>
        <input
          class="form-control"
          style={enter}
          type="text"
          placeholder="Search Technology..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        />
      </div>

      <div style={body}>
        {know
          .filter((point) => {
            if (searchTerm === "") {
              return point;
            } else if (
              point.technology.toLowerCase().includes(searchTerm.toLowerCase())
            ) {
              return point;
            }
          })
          .map((point) => (
            <Card style={card}>
              <Card.Body>
                {startWith(point.link) ? (
                  <ReactPlayer
                    url={point.link}
                    width="282px"
                    height="159px"
                    muted="false"
                    playing="true"
                  ></ReactPlayer>
                ) : (
                  <img
                    src={CardImg}
                    style={{
                      width: "318px",
                      height: "159px",
                      marginLeft: "-16px",
                    }}
                    alt="..."
                  ></img>
                )}

                <Card.Header>
                  <Card.Title>{point.technology}</Card.Title>
                </Card.Header>

                <Card.Subtitle
                  className="mb-2 text-muted"
                  style={{ marginTop: "10px" }}
                >
                  {point.title}
                </Card.Subtitle>
                <Card.Text>{point.description}</Card.Text>
                <footer className="blockquote-footer">{point.user}</footer>
                <a
                  href={point.link}
                  className="btn btn-secondary me-2"
                  target="_"
                >
                  Link
                </a>
                <Button
                  variant="primary"
                  onClick={() =>
                    dispatch(
                      deleteIdea({ technology: point.technology, id: point.id })
                    )
                  }
                >
                  Delete
                </Button>
              </Card.Body>
            </Card>
          ))}
      </div>
    </section>
  );
}

export default SmallCard;
