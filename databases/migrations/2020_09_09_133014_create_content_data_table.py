from orator.migrations import Migration


class CreateContentDataTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('content_data') as table:
            table.increments('id')
            table.integer('parent_id')
            table.small_integer('time')
            table.decimal('data_1', 10, 6)
            table.decimal('data_2', 10, 6)
            table.decimal('data_3', 10, 6)
            table.decimal('data_4', 10, 6)
            table.decimal('data_5', 10, 6)
            table.decimal('data_6', 10, 6)
            table.decimal('data_7', 10, 6)
            table.decimal('data_8', 10, 6)
            table.decimal('data_9', 10, 6)
            table.decimal('data_10', 10, 6)
            table.decimal('data_11', 10, 6)
            table.decimal('data_12', 10, 6)
            table.decimal('data_13', 10, 6)
            table.decimal('data_14', 10, 6)
            table.decimal('data_15', 10, 6)
            table.decimal('data_16', 10, 6)
            table.timestamps()
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('content_data')
