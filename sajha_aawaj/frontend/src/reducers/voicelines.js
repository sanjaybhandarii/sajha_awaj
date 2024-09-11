import { GET_LISTEN_SNIPPET, GET_LISTEN_SNIPPETS, PUT_LISTEN_SNIPPET, GET_RECORD_SNIPPETS, GET_RECORD_SNIPPET, PUT_RECORD_SNIPPET, ADD_SPEAKER } from "../actions/types";

const initialState = {
    snippets: [],
    speaker: [],
    snippet: {}
};

export default function(state = initialState, action) {

    switch (action.type) {
        case GET_RECORD_SNIPPETS:
        case GET_LISTEN_SNIPPETS:
            return {
                ...state,
                snippets: action.payload
            }

        case GET_RECORD_SNIPPET:
        case GET_LISTEN_SNIPPET:
            return {
                ...state,
                snippet: action.payload
            }

        case PUT_LISTEN_SNIPPET:
        case PUT_RECORD_SNIPPET:
            return {
                ...state,
                snippet: action.payload
            }


        case ADD_SPEAKER:
            return {
                ...state,
                speaker: action.payload
            }

        default:
            return state;
    }
}