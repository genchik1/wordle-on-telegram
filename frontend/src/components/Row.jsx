import {Box, Grid, Typography} from "@mui/material";
import {cssVar} from "../utils.js";


function BoxKey({id, backgroundColor, textColor, child}) {
    return <Box id={id} sx={{
        backgroundColor: backgroundColor,
        textAlign: 'center',
        color: textColor,
        borderRadius: "5px",
        height: "46px",
        width: "46px",
        fontSize: 20,
        borderColor: cssVar('--button-color'),
    }}>
        <Typography
            variant='h6'
            sx={{textTransform: 'uppercase', textAlign: 'center', paddingTop: "8px"}}
        >
            {child}
        </Typography>
    </Box>
}


export function FormRow({backgroundColor, textColor, state, line}) {
    return (
        <>
            <Grid item xs={1} sm={2} md={2}>
                <BoxKey id={`item_${line}_${1}`} backgroundColor={backgroundColor} textColor={textColor} child={
                    state[0]
                }/>
            </Grid>
            <Grid item xs={1} sm={2} md={2}>
                <BoxKey id={`item_${line}_${2}`} backgroundColor={backgroundColor} textColor={textColor} child={
                    state[1]
                }/>
            </Grid>
            <Grid item xs={1} sm={2} md={2}>
                <BoxKey id={`item_${line}_${3}`} backgroundColor={backgroundColor} textColor={textColor} child={
                    state[2]
                }/>
            </Grid>
            <Grid item xs={1} sm={1} md={2}>
                <BoxKey id={`item_${line}_${4}`} backgroundColor={backgroundColor} textColor={textColor} child={
                    state[3]
                }/>
            </Grid>
            <Grid item xs={1} sm={1} md={2}>
                <BoxKey id={`item_${line}_${5}`} backgroundColor={backgroundColor} textColor={textColor} child={
                    state[4]
                }/>
            </Grid>
        </>
    );
}