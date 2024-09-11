import axios from 'axios'
import { GET_LISTEN_SNIPPET, GET_LISTEN_SNIPPETS, PUT_LISTEN_SNIPPET, GET_ERRORS, GET_RECORD_SNIPPET, GET_RECORD_SNIPPETS, ADD_SPEAKER } from './types'
import { createMessages, returnErrors } from './messages'

export const getListenSnippets = () => (dispatch, getState) => {
    axios.get(`/api/snippet_listen`)
        .then(res => {
            dispatch({
                type: GET_LISTEN_SNIPPETS,
                payload: res.data
            })
        })
        .catch(err => dispatch(returnErrors(err.response.data, err.response.status)));
}

export const getListenSnippet = (id) => (dispatch, getState) => {
    axios.get(`/api/snippet_listen/${id}`)
        .then(res => {
            dispatch({
                type: GET_LISTEN_SNIPPET,
                payload: res.data
            })
        })
        .catch(err => dispatch(returnErrors(err.response.data, err.response.status)));
}

export const putListenSnippet = (id, data) => (dispatch, getState) => {

    const body = JSON.stringify(data);
    axios.put(`/api/snippet_listen/${id}`, body)
        .then(res => {
            dispatch({
                type: PUT_LISTEN_SNIPPET,
                payload: res.data
            })
        })
        .catch(err => dispatch(returnErrors(err.response.data, err.response.status)));
}

export const getRecordSnippet = (id) => (dispatch, getState) => {
    axios.get(`/api/snippet_record/${id}`)
        .then(res => {
            dispatch({
                type: GET_RECORD_SNIPPET,
                payload: res.data
            })
        })
        .catch(err => dispatch(returnErrors(err.response.data, err.response.status)));
}

export const getRecordSnippets = () => (dispatch, getState) => {
    axios.get(`/api/snippet_record/`)
        .then(res => {
            dispatch({
                type: GET_RECORD_SNIPPETS,
                payload: res.data
            })
        })
        .catch(err => dispatch(returnErrors(err.response.data, err.response.status)));
}

export const putRecordSnippet = (id, data) => (dispatch, getState) => {

    const body = JSON.stringify(data);
    axios.put(`/api/snippet_record/${id}/`, body)
        .then(res => {
            dispatch({
                type: PUT_RECORD_SNIPPET,
                payload: res.data
            })
        })
        .catch(err => dispatch(returnErrors(err.response.data, err.response.status)));
}


export const addSpeaker = (data) => (dispatch, getState) => {

    const body = JSON.stringify(data)
    axios
        .post(`/api/speaker/`, body)
        .then((res) => {
            dispatch({
                type: ADD_SPEAKER,
                payload: res.data
            });
        })
        .catch(err => dispatch(returnErrors(err.response.data, err.response.status)));

}