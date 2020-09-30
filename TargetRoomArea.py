from Autodesk.Revit.DB import FilteredElementCollector, FilteredElementIdIterator
from Autodesk.Revit.UI import TaskDialog
from rpw.ui.forms import TextInput
from Autodesk.Revit.DB.Architecture import Room, RoomFilter

doc = __revit__.ActiveUIDocument.Document
Target = TextInput('Enter Target Area', default="2303")
Target = float(Target)
RmFilter = RoomFilter()
collector = FilteredElementCollector(doc)
collector.WherePasses(RmFilter)
roomIdItr = collector.GetElementIdIterator()
roomIdItr.Reset()
prompt = 'The rooms that are smaller than ' + str(Target) + ' are:'
count = 0
while (roomIdItr.MoveNext()):
    roomId=roomIdItr.Current
    room = doc.GetElement(roomId)
    if (room.Area<Target):
        rmname = room.LookupParameter("Name").AsString()
        prompt += '\n' + rmname
        count += 1
if count == 0:
    prompt = 'No room found'
    print (prompt)
else:
    print ('Total rooms that are smaller than ' + str(Target) + ' is: '+ str(count))
    print (prompt)