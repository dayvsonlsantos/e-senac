const express = require('express');
const app = express();
const projectRoutes = express.Router();

let Project = require ('../model/Project');

app.use(express.json());

// API to add project
projectRoutes.post('/add', function (req, res) {
    let project = new Project(req.body);
    project.save()
    .then(project => {
        res.status(200).json({'status':'sucess', 'msg':'project added successfully'})
        // res.send(project);
    })
    .catch(err => {
        res.status(409).json({'status':'failure', 'msg':'unable to sabe to database'})
    });
});

// API to get projects
projectRoutes.get('/', function (req, res) {
    Project.find()
    .then(projects => {
        res.status(200).json({'status': 'success','projects': projects});
    })
    .catch(err => {
        res.status(400).send({'status': 'failure','mssg': 'Something went wrong'});
    })
})

// API to get project by ID
projectRoutes.get('/:id', (req, res) => {
    Project.findById(req.params.id)
    .then(project => {
        if (!project) {
            return res.status(404).json({'status':'failure', 'msg':'Project not found'});
        }
        res.status(200).json(project);
    })
    .catch(err => {
        console.log(err);
        res.status(500).json({'status':'failure', 'msg':'Internal server error'});
    });
});

// API to update project by ID
projectRoutes.put('/update/:id', (req, res) => {
    Project.findByIdAndUpdate(req.params.id, req.body, { new: true })
    // Esse new: True -> garante que o Mongoose retorne o documento atualizado, e não o original.
    .then(project => {
        if(!project){
            return res.status(404).json({'status':'failure', 'msg':'Project not found'});
        }
        res.status(200).json(project);
    })
    .catch(err => {
        console.log(err);
        res.status(500).json({'status':'failure', 'msg':'Internal server error'});
    });
})

// API to delete project by ID
projectRoutes.delete('/delete/:id', (req, res) => {
    Project.findByIdAndRemove({_id: req.params.id})
    .then(project => {
        if(!project){
            return res.status(404).json({'status':'failure', 'msg':'Project not found'});
        }
        res.status(200).json({'status':'success', 'msg':'Delete successfully'})
    })
    .catch(err => {
        res.status(400).send({'status': 'failure','mssg': 'Something went wrong'});
    });
})

module.exports = projectRoutes;