-- THIS FILE INCLUDE TRIGGERS FOR MAKE JOURNAL
-- trigger for Consumers, insert message in ConsumersLogs table
CREATE TRIGGER consumers_trigger AFTER INSERT ON Consumers
BEGIN
    INSERT INTO ConsumersLogs VALUES('');
END;

-- trigger
