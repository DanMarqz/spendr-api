import os
from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException
from pymongo import MongoClient
from bson.objectid import ObjectId
from fastapi.responses import JSONResponse

from api.models.transactions_model import TransactionModel

load_dotenv()
uri = os.environ['MONGO_URI']
client = MongoClient(uri)
expensesCollection = client.budgetAdmin.expenses

router = APIRouter()

def findExpense(id):
    expense = expensesCollection.find_one({'_id': ObjectId(id)})
    if expense is None:
        raise HTTPException(status_code=404, detail="Expense not found")

    return expense

@router.get("/transactions")
def getExpenses():
    expenses = []
    for doc in expensesCollection.find():
        expense = TransactionModel(**doc)
        expenses.append(expense.dict())
    return expenses


@router.get("/transaction/{id}")
def getExpense(id):
    expense = findExpense(id)
    expense = TransactionModel(**expense)
    return expense.dict()

@router.post("/transactions")
def createExpenses(expenses: TransactionModel):
    if not expenses.is_valid():
        raise HTTPException(status_code=400, detail="The expense data is not valid")
    
    result = expensesCollection.insert_one({
        'description': expenses.description,
        'date': expenses.date,
        'price': expenses.price,
        'category': expenses.category
    })
    return JSONResponse(str(result.inserted_id))

@router.delete("/transactions/{id}")
def deleteExpense(id):
    expense = findExpense(id)

    expensesCollection.delete_one({'_id': ObjectId(id)})
    return JSONResponse({
        'msg': 'Expense deleted',
    })

@router.put("/transactions/{id}")
def updateExpense(id, expenses: TransactionModel):
    expense = findExpense(id)

    expensesCollection.update_one({'_id': ObjectId(id)}, {"$set": expenses.dict()})
    return JSONResponse({
        'msg': 'Expense updated',
    })
