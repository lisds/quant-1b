test = {
  'name': 'Question 1.1.3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> genre_and_distances.head()['Genre'].value_counts().loc[my_assigned_genre] >= 3
          True
          >>> my_assigned_genre_was_correct == (my_assigned_genre == 'Country')
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
