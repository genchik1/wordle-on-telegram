import {Box} from "@mui/material";
import {cssVar} from "../utils.js";


export function Title() {
    // return <Typography sx={{marginBottom: "20px"}}> 5 БУКВ </Typography>
    let style = {
        height: "26px", width: "26px",
        backgroundColor: cssVar("--button-color"),
        color: cssVar("--button-text-color"),
        fontWeight: "bold",
        fontSize: 18,
        margin: "2px",
        borderRadius: "4px",
        display: 'inline-block',
    }
    return <Box sx={{display: 'block', marginBottom: "26px"}}>
        <Box sx={style}>5</Box>
        <Box sx={style}>Б</Box>
        <Box sx={style}>У</Box>
        <Box sx={style}>К</Box>
        <Box sx={style}>В</Box>
    </Box>
}
