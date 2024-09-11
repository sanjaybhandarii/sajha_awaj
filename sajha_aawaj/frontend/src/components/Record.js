import React, { Component, useEffect, useState } from 'react'
import { connect } from 'react-redux'
import { Link , Redirect} from 'react-router-dom'
import PropTypes from 'prop-types'

import { getRecordSnippets } from '../actions/voicelines'


export const Record = (props) => {

    useEffect(() => {
        props.getRecordSnippets();
      }, []);

  return (
    <div>Record</div>
  )
}

Record.propTypes = {
  snippets: PropTypes.object.isRequired,
}

const mapStateToProps = (state) => ({
    snippets: state.voicelines.snippets,
})


export default connect(mapStateToProps, { getRecordSnippets })(Record)