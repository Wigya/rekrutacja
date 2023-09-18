import { Box, Button, Dialog, TextField, Tooltip } from "@mui/material";
import CloseIcon from "@mui/icons-material/Close";
import React, { useEffect, useState } from "react";
import "./App.css";
import EditIcon from "@mui/icons-material/Edit";
import FavoriteIcon from "@mui/icons-material/Favorite";
import { dogFactsService } from "./services/dogFactsService";
import { favoriteService } from "./services/favoriteService";

function App() {
  const [dogFact, setDogFact] = useState("");
  const [favorites, setFavorites] = useState<Array<string>>([]);
  const [changed, setChanged] = useState(0);
  const [dialogOpen, setDialogOpen] = useState(false);
  const [chosenQuestion, setChosenQuestion] = useState("");
  const [updatedQuestion, setUpdatedQuestion] = useState("");
  const handleGenerateFact = async () => {
    let resp = (await dogFactsService.getFact().then((response) => response))
      .data;

    setDogFact(() => resp.payload);
  };

  const handleUpdate = async (favorite: any, newFavorite: any) => {
    favoriteService.updateFavorite({
      original: favorite,
      newValue: newFavorite,
    });
    setChanged((prev) => prev + 1);
  };

  const handleAddFavorite = async () => {
    await favoriteService
      .addFavorite({ data: dogFact })
      .then((response: any) => response);

    setChanged((prev) => prev + 1);
  };

  useEffect(() => {
    async function fetchData() {
      let resp = await favoriteService
        .getFavorites()
        .then((response) => response);
      setFavorites(() => resp.data);
    }

    fetchData();
  }, [changed]);

  const handleDelete = (text: string) => {
    favoriteService.deleteFavorite(text);
    setChanged((prev) => prev + 1);
  };

  return (
    <div className="app">
      <Dialog
        open={dialogOpen}
        onClose={() => setDialogOpen(false)}
        style={{
          display: "flex",
          justifyContent: "center",
          justifyItems: "center",
        }}
      >
        <div
          style={{
            width: "400px",
            height: "400px",
            display: "flex",
            justifyItems: "center",
            flexDirection: "column",
          }}
        >
          <h1 style={{ textAlign: "center" }}>Edit quote</h1>
          <TextField
            value={updatedQuestion}
            style={{
              width: "300px",
              height: "80px",
              marginLeft: "50px",
              marginTop: "80px",
            }}
            onChange={(e) => {
              setUpdatedQuestion((prev) => e.target.value);
            }}
          />
          <div
            style={{
              marginLeft: "auto",
              marginRight: "20px",
              marginTop: "auto",
              marginBottom: "20px",
            }}
          >
            <Button onClick={() => setDialogOpen(false)}>Cancel</Button>
            <Button
              onClick={() => {
                handleUpdate(chosenQuestion, updatedQuestion);
                setDialogOpen(false);
              }}
            >
              Submit
            </Button>
          </div>
        </div>
      </Dialog>

      <Box
        bgcolor="pink"
        width="550px"
        height="350px"
        padding={"30px"}
        display={"flex"}
        flexDirection={"column"}
        overflow={"auto"}
      >
        <h1 style={{ marginLeft: "auto", marginRight: "auto" }}>Favorites</h1>
        {favorites.map((favorite, index) => {
          return (
            <div
              style={{
                width: "100%",
                height: "50px",
                display: "flex",
              }}
              key={index}
            >
              <Box
                sx={{
                  overflow: "auto",
                  width: "90%",
                  height: "40px",
                  marginRight: "10px",
                  marginTop: "10px",
                }}
              >
                {favorite}
              </Box>
              <Button
                style={{ height: "40px", width: "40px" }}
                onClick={() => {
                  setDialogOpen((prev) => !prev);
                  setChosenQuestion(favorite);
                  setUpdatedQuestion(favorite);
                }}
              >
                <EditIcon />
              </Button>
              <Button
                style={{ height: "40px", width: "40px" }}
                onClick={() => handleDelete(favorite)}
              >
                <CloseIcon color="error" />
              </Button>
            </div>
          );
        })}
      </Box>
      <div className="center-box">
        <Box
          bgcolor={"rgb(251, 146, 60)"}
          width={"550px"}
          height={"350px"}
          padding={"30px"}
        >
          <h1>Random dog fact</h1>

          <Box height="100px" whiteSpace="pre-wrap" marginTop="50px">
            {dogFact}
          </Box>
          <div id="buttons">
            <Button
              variant="contained"
              style={{
                fontWeight: 600,
                paddingBottom: "20px",
                paddingTop: "20px",
              }}
              onClick={handleGenerateFact}
            >
              Generate
            </Button>
            <Tooltip title="Add to favorite" placement="top" arrow>
              <Button
                variant="contained"
                style={{
                  backgroundColor: "pink",
                  paddingBottom: "15px",
                  paddingTop: "15px",
                  marginLeft: "30px",
                }}
                onClick={handleAddFavorite}
              >
                <FavoriteIcon fontSize="large" sx={{ color: "red" }} />
              </Button>
            </Tooltip>
          </div>
        </Box>
      </div>
    </div>
  );
}

export default App;
