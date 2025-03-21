test = {
  'name': 'Question 02_gender_by_survived',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'gender_by_survived'
          >>> 'gender_by_survived' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'gender_by_survived'
          >>> # from its initial state (of ...)
          >>> gender_by_survived is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # The values in the table should be counts.
          >>> np.all(np.array(gender_by_survived) > 1)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> isinstance(gender_by_survived, pd.DataFrame)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> gender_by_survived.shape
          (2, 2)
          """,
          'hidden': False,
          'locked': False
        },
        #: begin-extra
        {
          'code': r"""
          >>> list(gender_by_survived) == ['no', 'yes']
          True
          >>> list(gender_by_survived.T) == ['female', 'male']
          True
          >>> np.allclose(gender_by_survived, [[130, 359], [1366, 352]])
          True
          """,
          'hidden': False,
          'locked': False
        },
        #: end-extra
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
