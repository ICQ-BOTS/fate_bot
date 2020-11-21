box.cfg{
    listen=3301
}

box.schema.user.grant('guest', 'read,write,execute', 'universe', nil, {if_not_exists=true})
box.once("fate", function()
    box.schema.sequence.create('default_S')
    box.schema.space.create('default', {
        if_not_exists = true,
        format={
            {name = 'id', type = 'unsigned'},
            {name = 'answer', type = 'string'}
        }
    })
    box.space.default:create_index('id', {
        sequence = 'default_S',
        parts = {'id'}
    }) 

    box.schema.sequence.create('prophecy_S')
    box.schema.space.create('prophecy', {
        if_not_exists = true,
        format={
            {name = 'id', type = 'unsigned'},
            {name = 'answer', type = 'string'}
        }
    })
    box.space.prophecy:create_index('id', {
        sequence = 'prophecy_S',
        parts = {'id'}
    }) 

    box.schema.sequence.create('number_S')
    box.schema.space.create('number', {
        if_not_exists = true,
        format={
            {name = 'id', type = 'unsigned'},
            {name = 'start_answer', type = 'string'}
        }
    })
    box.space.number:create_index('id', {
        sequence = 'number_S',
        parts = {'id'}
    }) 

    box.schema.sequence.create('color_S')
    box.schema.space.create('color', {
        if_not_exists = true,
        format={
            {name = 'id', type = 'unsigned'},
            {name = 'type', type = 'string'},
            {name = 'answer', type = 'string'}
        }
    })
    box.space.color:create_index('id', {
        sequence = 'color_S',
        parts = {'id'}
    })
    box.space.color:create_index('type', {
        parts = {'type'},
        if_not_exists = true,
        unique = false
    })
end
)


