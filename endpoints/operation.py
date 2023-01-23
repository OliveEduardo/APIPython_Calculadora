from fastapi import APIRouter
from models.request import OperationRequest
from models.response import Response
from models.models import Operacao
from db.database import Database

router = APIRouter(
    prefix="/calculadora",
    tags=["Calculadora"],
    responses={404: {"description": "Not found"}},
)

database = Database()
engine = database.get_db_connection()


@router.post("/soma", response_description="soma de dois operadores")
async def soma(operation_req: OperationRequest):
    new_operation = Operacao()
    new_operation.name = "soma"
    new_operation.resultado = operation_req.n1 + operation_req.n2
    session = database.get_db_session(engine)
    session.add(new_operation)
    session.flush()
    session.refresh(new_operation, attribute_names=['id'])
    data = {"operation_id": new_operation.id, "resultado" : new_operation.resultado}
    session.commit()
    session.close()
    return Response(data, 200, "Operação adicionada com sucesso.", False)

@router.post("/subtracao", response_description="subtração de dois operadores")
async def subtracao(operation_req: OperationRequest):
    new_operation = Operacao()
    new_operation.name = "subtracao"
    new_operation.resultado = operation_req.n1 - operation_req.n2
    session = database.get_db_session(engine)
    session.add(new_operation)
    session.flush()
    session.refresh(new_operation, attribute_names=['id'])
    data = {"operation_id": new_operation.id}
    session.commit()
    session.close()
    return Response(data, 200, "Operation added successfully.", False)


@router.post("/multiplicacao", response_description="multiplicação de dois operadores")
async def multiplicacao(operation_req: OperationRequest):
    new_operation = Operacao()
    new_operation.name = "multiplicacao"
    new_operation.resultado = operation_req.n1 * operation_req.n2
    new_operation_id = None
    session = database.get_db_session(engine)
    session.add(new_operation)
    session.flush()

    session.refresh(new_operation, attribute_names=['id'])
    data = {"operation_id": new_operation.id}
    session.commit()
    session.close()
    return Response(data, 200, "Operation added successfully.", False)


@router.post("/divisao", response_description="divisão de dois operadores")
async def divisao(operation_req: OperationRequest):
    new_operation = Operacao()
    new_operation.name = "divisao"
    new_operation.resultado = operation_req.n1 / operation_req.n2
    session = database.get_db_session(engine)
    session.add(new_operation)
    session.flush()
    session.refresh(new_operation, attribute_names=['id'])
    data = {"operation_id": new_operation.id}
    session.commit()
    session.close()
    return Response(data, 200, "Operation added successfully.", False)


@router.get("/operacoes")
async def read_all():
    session = database.get_db_session(engine)
    data = session.query(Operacao).all()
    return Response(data, 200, "Operações retornadas com sucesso", False)