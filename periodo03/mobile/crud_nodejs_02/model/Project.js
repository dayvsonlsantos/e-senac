const mongoose = require('mongoose')
const Schema = mongoose.Schema;

let Project = new Schema({
    projectName: {
        type: String
    },
    projectDescription: {
        type: String
    },
    projectEndDate: {
        type: Date
    },
    projectURL: {
        type: String
    },
    projectShareLink: {
        type: String
    },
    projectRepository: {
        type: String
    }
},{
    collection: 'projects_cl'
})

module.exports = mongoose.model('Project', Project);