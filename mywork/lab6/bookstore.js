// Task 2: use database
// <paste your use bookstore>
use bookstore
// Task 3: insert first author
// <paste your insertOne>
db.authors.insertOne({
  "name": "Jane Austen",
  "nationality": "British",
  "bio": {
    "short": "English novelist known for novels about the British landed gentry.",
    "long": "Jane Austen was an English novelist whose works critique and comment upon the British landed gentry at the end of the 18th century. Her most famous novels include Pride and Prejudice, Sense and Sensi>
  }
})
// Task 4: update to add birthday
// <paste your updateOne>
db.authors.updateOne({ name: "Jane Austen" }, { $set: { birthday: '1775-12-16' } })
// Task 5: insert four more authors
// <paste your insertMany or insertOne x4>
db.authors.insertOne({
  name: 'Victor Hugo',
  nationality: 'French',
  bio: {
    short: 'French author, poet, playright, and human rights activist.',
    long: 'Victor Hugo is a French romantist who wrote books, plays, poems, journals, essays. His well known works are The Hunchback of Notre Dame and Les Miserables.'
  },
  birthday: '1802-02-26'
})
db.authors.insertOne({
  name: 'Miguel de Cervantes',
  nationality: 'Spanish',
  bio: {
    short: 'Spanish writer, poet, and playwright',
    long: 'Miguel de Cervantes was a Spanish writer often called The Prince of Satire who was most well known for his novel Don Quixote de la Mancha.'
  },
  birthday: '1547-09-29'
})
db.authors.insertOne({
  name: 'Mark Twain',
  nationality: 'American',
  bio: {
    short: 'Well known author and essayist.',
    long: 'Mark Twain was a very well known author best known for their books The Adventures of Huckleberry Finn and The Adventures of Tom Sawyer.'
  },
  birthday: '1835-11-30'
})
db.authors.insertOne({name: 'Machado de Assis', nationality: 'Brazilian', bio: {short: 'Brazilian novelist, poet, and playwright.', long: 'Often called the greatest writer of Brazilian literature, Joaquim Maria M>
// Task 6: total count
// <paste your countDocuments>
db.authors.countDocuments()
// Task 7: British authors, sorted by name
// <paste your find + sort>
db.authors.find({nationality: "British"}).sort({name: 1})
