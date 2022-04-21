import searchIcon from "./search-icon.png";

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
  width: "490px",
  height: "55px",
  color: "gray",
  backgroundImage: `url(${searchIcon})`,
  backgroundPosition: "9px 17px",
  backgroundRepeat: "no-repeat",
  backgroundSize: "21px 19px",
  backgroundColor: "#f9f9f9",
  paddingLeft: "39px",
  outline: "none",
  boxShadow: "0 0 12px rgba(0,0,0,0.5)",
  borderColor: "transparent",
  marginTop: "33px",
};
