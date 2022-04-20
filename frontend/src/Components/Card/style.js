import searchIcon from "./searchicon.png";

export const body = {
  display: "flex",
  flexDirection: "row",
  justifyContent: "center",
  gap: "47px 77px",
  flexWrap: "wrap",
  marginTop: "49px",
};

export const card = {
  width: "20rem",
  boxShadow: "0 0 12px rgba(0,0,0,0.5)",
  borderRadius: "15px",
};

export const search = {
  display: "flex",
  justifyContent: "center",
};

export const enter = {
  width: "415px",
  height: "55px",
  color: "white",
  backgroundImage: `url(${searchIcon})`,
  backgroundPosition: "9px 19px",
  backgroundRepeat: "no-repeat",
  backgroundSize: "15px 16px",
  backgroundColor: "#f9f9f9",
  paddingLeft: "33px",
};
