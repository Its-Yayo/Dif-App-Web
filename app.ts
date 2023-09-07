import express, { request, response } from 'express';

const app = express();
const port = 3000;
app.use(express.json());

app.get('/', (req: Request, res: Response) => {
    res.send('TODO implementation');
});

app.listen(port, () => {
    console.log('Server is listening on port 3000');
});